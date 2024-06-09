import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Artifacts() {
  const [artifacts, setArtifacts] = useState([]);
  const [newArtifact, setNewArtifact] = useState({ title: '', description: '' });

  useEffect(() => {
    fetchArtifacts();
  }, []);

  const fetchArtifacts = async () => {
    try {
      const response = await axios.get('/artifacts');
      setArtifacts(response.data);
    } catch (error) {
      console.error('Error fetching artifacts:', error);
      // Handle error (e.g., display error message)
    }
  };

  const handleChange = (e) => {
    setNewArtifact({ ...newArtifact, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('/artifacts', newArtifact);
      fetchArtifacts(); // Refresh list after successful creation
      setNewArtifact({ title: '', description: '' }); // Clear form
    } catch (error) {
      console.error('Error creating artifact:', error);
      // Handle error (e.g., display error message)
    }
  };

  const handleDeleteArtifact = async (artifactId) => {
    try {
        await axios.delete(`/artifacts/${artifactId}`); // Delete request with artist ID
        const remainingArtifacts = artifacts.filter(artifact => artifact.id !== artifactId);
        setArtifacts(remainingArtifacts);
    } catch (error) {
        console.error('Error deleting artifact:', error);
        // Handle error appropriately (e.g., display error message to the user)
    }
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
      <ol>
        {artifacts.map((artifact) => (
          <li key={artifact.id}>
            {artifact.title} - {artifact.description}
            <button onClick={() => handleDeleteArtifact(artifact.id)}>
              Delete
            </button>
          </li>
        ))}
      </ol>
    </div>
  );
}

export default Artifacts;
