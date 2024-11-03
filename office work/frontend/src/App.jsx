
// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import NavBar from './NavBar';
import Home from './Home';
import About from './About';
import SystemDataChart from './SystemDataChart';
import Services from './Services';
import ServiceRefresh from './ServiceRefresh';
import Contact from './Contact';
import './App.css';
import ServerMap from './ServerMap';

function App() {
  return (
    <Router>
      <div className="App">
        <NavBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/ServerMap" element={<ServerMap />} />
          <Route path="/about" element={<About />} />
          <Route path="/services" element={<Services />} />
          <Route path="/ServiceRefresh" element={<ServiceRefresh />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/SystemDataChart" element={<SystemDataChart />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
