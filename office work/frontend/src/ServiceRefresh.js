import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ServiceRefresh = () => {
  const [data, setData] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/refresh_log')
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
  if (error) return <p>Error loading data: {error.message}</p>;

  return (
    <div>
      <h2>EMS Service Check</h2>
      <ul>
        {Object.entries(data).map(([logFile, statuses]) => (
          <li key={logFile}>
            <strong>{logFile}</strong>
            <ul>
              {Object.entries(statuses).map(([statusType, statusValue]) => (
                <li key={statusType}>{statusType}: {statusValue}</li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ServiceRefresh;
