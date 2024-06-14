import React,{useState} from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import WebCam from './components/WebCam';
import Tutorial from './components/Tutorial';
import Home from './components/Home';
import About from './components/About';
import Contact from './components/Contact';
import Navbar from './components/Navbar';
import './styles/index.css';

const App = () => {

  const [onCam, setOnCam] = useState(false);

  return (
    <Router>
      <div className="App">
        {!onCam && <Navbar setOnCam={setOnCam}/>}
        <div id='home-section'>
          <Routes>
            <Route path="/" element={<Home setOnCam={setOnCam}/>} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
          </Routes>
        </div>
        <Routes>
          <Route path="/american" element={<WebCam sign_type='american'/>} />
          <Route path="/indian" element={<WebCam sign_type='indian' />} />
          <Route path="/gestures" element={<WebCam sign_type='gesture' />} />
          <Route path="/tutorial" element={<Tutorial />} />
        </Routes>
        {!onCam && (<footer className="footer">
          <p className="footer-text">Copyright © 2024 - Sign Language Recognition</p>
        </footer>)}
      </div>
    </Router>
  );
};

export default App;
