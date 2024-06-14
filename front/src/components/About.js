import React from 'react';
import img from '../images/business-meeting.avif'

const About = () => {
  return ( 
    <div className='about-div'>
      <h1 style={{marginBottom:70,marginTop:50}}>About Us</h1>
      <div style={{display:'flex', justifyContent:'space-between'}}>
      <div>
        <p>Welcome to our Sign Language Recognition platform! Our mission is to create an inclusive and accessible environment by leveraging technology to facilitate communication for individuals who are deaf or hard of hearing.</p>
        <br />
        <p>Our team consists of passionate individuals. Together, we are dedicated to developing innovative solutions that bridge the communication gap and empower individuals to express themselves freely.</p>
        <br />
        <p>With our expertise in machine learning, and computer vision, we have developed state-of-the-art algorithms capable of accurately recognizing and interpreting sign language gestures in real-time. Our goal is to make sign language recognition technology widely accessible and user-friendly, enabling seamless communication between individuals who use sign language and those who may not be familiar with it.</p>
      </div>
      <img src={img} alt="business-meeting" style={{marginRight:20,width:600}}/>
      </div>
    </div>
  );
}

export default About;
