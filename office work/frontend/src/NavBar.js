// src/NavBar.js
import React from 'react';
import { Link } from 'react-router-dom';
import './NavBar.css';

const NavBar = () => {
  return (
    <nav className="navbar">
      <h1 className="navbar-logo">MyApp</h1>
      <ul className="navbar-links">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/about">About</Link></li>
        <li><Link to="/services">Services</Link></li>
       <li><Link to="/ServiceRefresh">ServiceRefresh</Link></li>
        <li><Link to="/contact">Contact</Link></li>
        <li><Link to="/SystemDataChart">SystemDataChart</Link></li>
      </ul>
    </nav>
  );
}

export default NavBar;
