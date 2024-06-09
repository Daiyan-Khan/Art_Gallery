import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Artifacts() {
    const [artifacts, setArtifacts] = useState([]);
    const [newArtifact, setNewArtifact] = useState({ title: '', description: '' });

    useEffect(() => {
        
        fetchArtifacts();
        
    }, []);

    const fetchArtifacts = async () => {
        const response = await axios.get('/artifacts',{headers: {
            'Content-Type': 'application/json'
        }});
        
        setArtifacts(response.data);
    };

    const handleChange = (e) => {
        setNewArtifact({ ...newArtifact, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        await axios.post('/artifacts', newArtifact);
        fetchArtifacts();
        setNewArtifact({ title: '', description: '' });
    };

    return (
        <div>
            <h1>Artifacts</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    name="title"
                    value={newArtifact.title}
                    onChange={handleChange}
                    placeholder="Title"
                />
                <input
                    type="text"
                    name="description"
                    value={newArtifact.description}
                    onChange={handleChange}
                    placeholder="Description"
                />
                <button type="submit">Add Artifact</button>
            </form>
            <ul>
                {artifacts.map((artifact) => (
                    <li key={artifact.id}>
                        {artifact.name} - {artifact.description}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Artifacts;
