import React, { useState, useRef, useEffect } from 'react';
import Webcam from 'react-webcam';
import axios from 'axios';

function WebCam(props) {
  const [predictionValue, setPredictionValue] = useState(null);
  const [previousPrediction, setPreviousPrediction] = useState(null);
  const webcamRef = useRef(null);
  const textRef = useRef(null);

  const captureInterval = 3000;

  useEffect(() => {
    const captureFrames = async () => {
      if (!webcamRef.current || !webcamRef.current.video || !webcamRef.current.video.videoWidth) {
        return;
      }

      const imageDataURL = webcamRef.current.getScreenshot();

      try {
        const response = await axios.post('http://localhost:5000/predict', { image: imageDataURL, sign_type: props.sign_type });
        const {prediction} = response.data;
        if (prediction !== previousPrediction) {
          setPredictionValue(prediction);
          setPreviousPrediction(prediction);
          if (prediction !== 'no_hands') {
            const textArea = document.querySelector('.text');
            textArea.innerHTML += `${prediction}\n`;
          }
        }
      } 
      catch (error) {
        console.error('Error making POST request:', error);
      }

    };

    const intervalId = setInterval(captureFrames, captureInterval);

    return () => clearTimeout(intervalId);
  }, [props.sign_type,previousPrediction]);

  const clearText = () => {
    if (textRef.current) {
      textRef.current.innerText = ''; 
      setPreviousPrediction(null);
    }
  };

  useEffect(() => {
    const handleKeyPress = (event) => {
      if (event.keyCode === 32) {
        event.preventDefault();
        appendSpace(); 
      }
    };

    document.body.addEventListener('keydown', handleKeyPress);

    return () => {
      document.body.removeEventListener('keydown', handleKeyPress);
    };
  }, []);

  const appendSpace = () => {
    const textArea = document.querySelector('.text');
    if (textArea) {
      textArea.innerHTML += '&nbsp;';
    }
  };

  return (
    <div>
      <header className="App-header">
        <h1>
          {props.sign_type === 'american' ? 'American alphabets' : props.sign_type === 'indian' ? 'Indian alphabets' : 'Gestures'}
        </h1>
        <div className="CamAndSentence">
          <div className="Webcam-container">
            <Webcam ref={webcamRef} />
            <h2>Prediction: {(predictionValue !== 'no_hands')? predictionValue : ''}</h2>
          </div>
          <div className="textarea-container">
            <h2>Sentence:</h2>
            <p ref={textRef} className='text'></p>
          </div>
          <button onClick={() => clearText()} className="clear-button">
              Clear text
          </button>
        </div>
      </header>
    </div>
  );
}

export default WebCam;
