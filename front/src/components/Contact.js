// Contact.js
import React from 'react';
import mail from "../images/mail.png";
import github from "../images/github.png";
import linkedin from "../images/linkedin.png";

const Contact = () => {
  return (
    <div className='contact-container'>
      <h1 style={{paddingTop:50,marginBottom:70}}>Contact Us</h1>
      <p style={{marginBottom:50}}>If you have any questions, feedback, or inquiries, please feel free to reach out to us using the contact information below:</p>
      <div className="contact-info">
        <div className="member">
          <h3>S. Hari Chandana</h3> 
          <p>Email: sharichandana123@gmail.com</p>
          <p>GitHub: Harichandana3</p>
          <p>LinkedIn: somagutta-hari-chandana</p>
          <div className='contact-links'>
            <a href="mailto:sharichandana123@gmail.com"><img src={mail} alt="mail logo" className='mail-logo'/></a>
            <a href="https://github.com/Harichandana3"><img src={github} alt="github logo" className='github-logo'/></a>
            <a href="https://www.linkedln.com/in/somagutta-hari-chandana-97293123a"><img src={linkedin} alt="linkedin logo" className='linkedin-logo'/></a>
          </div>
        </div>
        <div className="member">
          <h3>P. Sasikumar</h3>
          <p>Email: peddakotlasasikumar@gmail.com</p>
          <p>GitHub: SasikumarPeddakotla</p>
          <p>LinkedIn: sasikumarpeddakotla</p>
          <div className='contact-links'>
            <a href="mailto:peddakotlasasikumar@gmail.com"><img src={mail} alt="mail logo" className='mail-logo'/></a>
            <a href="https://github.com/SasikumarPeddakotla"><img src={github} alt="github logo" className='github-logo'/></a>
            <a href="https://www.linkedin.com/in/sasikumarpeddakotla/"><img src={linkedin} alt="linkedin logo" className='linkedin-logo'/></a>
          </div>
        </div>
        <div className="member">
          <h3>M. Shankar</h3>
          <p>Email: mshankar2771@gmail.com</p>
          <p>GitHub: Shankar2771</p>
          <p>LinkedIn: shankarnaikmudavath</p>
          <div className='contact-links'>
            <a href="mailto:mshankar2771@gmail.com"><img src={mail} alt="mail logo" className='mail-logo'/></a>
            <a href="https://github.com/Shankar2771"><img src={github} alt="github logo" className='github-logo'/></a>
            <a href="https://www.linkedin.com/in/shankar-naik-mudavath-05b539251?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"><img src={linkedin} alt="linkedin logo" className='linkedin-logo'/></a>
          </div>
        </div>
      </div>
    </div>

  );
}

export default Contact;
