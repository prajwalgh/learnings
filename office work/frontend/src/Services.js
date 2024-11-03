// src/Services.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Services = () => {
  const [data, setData] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/ems-check') // replace with your actual API endpoint
      .then(response => {
        setData(response.data);
        setLoading(false);
      })
      .catch(error => {
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error loading data</p>;

  return (
    <div>
      <h2>Services</h2>
      <p>EMS Service Check</p>
      <ul>
        {Object.entries(data).map(([server, status]) => (
          <li key={server}>{server}: {status}</li>
        ))}
      </ul>
    </div>
  );
}

export default Services;
