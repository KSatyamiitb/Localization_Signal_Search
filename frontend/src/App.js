import './App.css';
import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [query1, setQuery1] = useState('');
    const [query2, setQuery2] = useState('');
    const [stringList, setSearchResults] = useState([]);

    const handleSubmit = async(event) => {
        event.preventDefault();
        try {
            // const response = await axios.get(`http://localhost:5000/search?query1=${query1}&query2=${query2}`);
            console.log(`sending reques to https://localization-signal-search-server.onrender.com/search?query1=${query1}&query2=${query2}`);
            const response = await axios.get(`https://localization-signal-search-server.onrender.com/search?query1=${query1}&query2=${query2}`);
            const data = response.data;
            const stringList = data.split('\n').map(line => line.trim()).filter(line => line !== '');
            setSearchResults(stringList);
        } catch (error) {
            console.error('Error fetching search results:', error);
        }
    };

    return (
        <div className="App">
          <header className="header">
            <h1>BB411 Assignment 2</h1>
            <h2>Search Localization Signal in Genes</h2>
          </header>
          <div className="form-container">
            <form onSubmit={handleSubmit}>
                <input
                    className="input-field"
                    type="text"
                    placeholder="Target Amino Acid Sequence"
                    value={query1}
                    onChange={(e) => setQuery1(e.target.value)}
                />
                <input
                    className="input-field"
                    type="text"
                    placeholder="Gene Names"
                    value={query2}
                    onChange={(e) => setQuery2(e.target.value)}
                />
                <button className="button" type="submit">Submit</button>
            </form>
          </div>

          <div className="results-container-header">'
            <header className="header">
                <h2>Localization Signal found in :</h2>
            </header>
            <ul className="results">
                {stringList.map((str, index) => (
                    <li key={index}>{str}</li>
                ))}
            </ul>
          </div>
        </div>
    );
}

export default App;
