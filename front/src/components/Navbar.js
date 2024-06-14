import React,{useEffect} from 'react';
import { Link, useLocation } from 'react-router-dom';
import '../styles/Navbar.css'; // Import your CSS file for styling

const Navbar = (props) => {
  const scrollToSection = (sectionId) => {
    console.log('Scrolling to section:', sectionId);
    const section = document.getElementById(sectionId);
    console.log('Section element:', section);
    if (section) {
      section.scrollIntoView({ behavior: 'smooth' });
    } 
  };

  const location = useLocation();
  

  useEffect(() => {
    const path = location.pathname;
    const isCameraPath = ['/american', '/indian', '/gestures', '/tutorial'].includes(path);
    props.setOnCam(isCameraPath);
  }, [location,props]);

  return (
    <nav className="navbar">
      <div className="background-image">
        <div className="overlay">
          <h1>Sign Language Recognition</h1>
        </div>
        <ul className="nav-links">
        <li>
          <Link to="/" onClick={() => scrollToSection('home-section')} className="nav-link">Home</Link>
        </li>
        <li>
          <Link to="/about" onClick={() => scrollToSection('home-section')} className="nav-link">About Us</Link>
        </li>
        <li>
          <Link to="/contact" onClick={() => scrollToSection('home-section')} className="nav-link">Contact Us</Link>
        </li>
      </ul>
      </div>
    </nav>
  );
}

export default Navbar;
