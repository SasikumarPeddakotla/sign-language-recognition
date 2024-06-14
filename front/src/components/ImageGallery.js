import React from 'react';
import '../styles/ImageGallery.css';

function ImageGallery(props) {

    const alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

    const gestures = ["Bye", "Call Me", "Good Luck", "Heart", "Hello", "Help", "I Love You", "Me", "Movie", "Not Okay",
    "Okay", "Perfect", "Smile", "Sorry", "Thank You", "You"]
      

  return (
    <div className="image-gallery-container">
        <div className="image-gallery">
        {`${props.sign}` === 'Gestures' ? 
            gestures.map((gesture, index) => (
                <div>
                    <img key={index} src={`${props.sign}/${gesture}.jpg`} alt={gesture} className='gesture_image'/>
                    <h2 className='gesture_label'>{gesture}</h2>
                </div>
            )) :
            alphabets.map((alphabet, index) => (
                <img key={index} src={`${props.sign}/${alphabet}.jpg`} alt={alphabet} className='alphabet_image'/>
            ))
        }

            {/* {alphabets.map((alphabet, index) => (
                <img key={index} src={`${props.sign}/${alphabet}`} alt={alphabet} />
            ))} */}
        </div>
    </div>
  );
}

export default ImageGallery;
