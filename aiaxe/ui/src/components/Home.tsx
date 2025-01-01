import { useState } from "react";
import "../App.css";

const Home = () => {
  const [isCollapsed, setIsCollapsed] = useState(false);

  const toggleNavbar = () => {
    setIsCollapsed(!isCollapsed);
  };

  return (
    <div className="navbar">
      <button
        className={`toggle-btn ${isCollapsed ? "collapsed" : ""}`}
        onClick={toggleNavbar}
      >
        {isCollapsed ? "▶" : "◀"}
      </button>
      <div className={`sidebar ${isCollapsed ? "collapsed" : ""}`}>
        {!isCollapsed && (
          <ul className="menu font-bold">
            <li>
              <a href="#home">Home</a>
            </li>
            <li>
              <a href="#services">Services</a>
            </li>
            <li>
              <a href="#about">About</a>
            </li>
          </ul>
        )}
      </div>
      <div className="content">
        <h1>Welcome to the website!</h1>
        <p>Click on the links in the navbar to navigate.</p>
      </div>
    </div>
  );
};

export default Home;
