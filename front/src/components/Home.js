import React,{useEffect} from 'react';
import { Link,useLocation } from 'react-router-dom';
import americanimg from '../images/americanA.jpg';
import indianimg from '../images/indianA.jpg'
import gestureimg from '../images/deaf-woman-communicating-through-sign-language.jpg'
import tutorialImg from '../images/tutorialImg.webp'

const Home = (props) => {

  const location = useLocation(); 

  useEffect(() => {
    const path = location.pathname;
    const isCameraPath = ['/american', '/indian', '/gestures', '/tutorial'].includes(path);
    props.setOnCam(isCameraPath);
  }, [location,props]);

  return (
      <div className='Home'>
        <h1>Select One</h1>
        <ul className="languages-items">
          <li className="languages-item">
            <Link to="/american" className="language-names">
              <img src={americanimg} alt='american A'/>
              <h1>American alphabets</h1>
            </Link>
          </li>
          <li className="languages-item">
            <Link to="/indian" className="language-names">
              <img src={indianimg} alt='american A' style={{height:300}}/>
              <h1>Indian alphabets</h1>
            </Link>
          </li>
          <li className="languages-item">
            <Link to="/gestures" className="language-names">
              <img src={gestureimg} alt='american A'/>
              <h1>Gestures</h1>
            </Link>
          </li>
          <li className="languages-item">
            <Link to="/tutorial" className="language-names">
              <img src={tutorialImg} alt='american A'/>
              <h1>Tutorial</h1>
            </Link>
          </li>
        </ul>
      </div>
  );
};

export default Home;
