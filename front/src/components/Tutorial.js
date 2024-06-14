import React,{useState} from "react";
import ImageGallery from "./ImageGallery";

function Tutorial(){
    const [activeButton, setActiveButton] = useState('button1');

    const handleButtonClick = (buttonId) => {
        setActiveButton(buttonId);
    };
    return(
        <div className="Tutorial">
            <h1>Tutorial</h1>
            <div className="toggle-buttons">
                <button
                    className={activeButton === 'button1' ? 'active' : 'notActive'}
                    onClick={() => handleButtonClick('button1')}
                >
                    American alphabets
                </button>
                <button
                    className={activeButton === 'button2' ? 'active' : 'notActive'}
                    onClick={() => handleButtonClick('button2')}
                >
                    Indian alphabets
                </button>
                <button
                    className={activeButton === 'button3' ? 'active' : 'notActive'}
                    onClick={() => handleButtonClick('button3')}
                >
                    Gestures
                </button>
            </div>
            {/* {activeButton === 'button1' && (<img src={american_signs} alt="american_signs" className="american_signs_img"/>)} */}
            {activeButton === 'button1' && (<ImageGallery folderPath="/American_alphabets/" sign='American_alphabets'/>)}
            {activeButton === 'button2' && (<ImageGallery folderPath="/Indian_alphabets/" sign='Indian_alphabets'/>)}
            {activeButton === 'button3' && (<ImageGallery folderPath="/Gestures/" sign='Gestures'/>)}
        </div>
    )
}

export default Tutorial;