import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Artists() {
    const [artists, setArtists] = useState([]);
    const [newArtist, setNewArtist] = useState({ name: '', bio: '' });

    useEffect(() => {
        fetchArtists();
    }, []);

    const fetchArtists = async () => {
        const response = await axios.get('/artists');
        setArtists(response.data);
    };

    const handleChange = (e) => {
        setNewArtist({ ...newArtist, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        await axios.post('/artists', newArtist);
        fetchArtists();
        setNewArtist({ name: '', bio: '' });
    };

    return (
        <div>
            <h1>Artists</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    name="name"
                    value={newArtist.name}
                    onChange={handleChange}
                    placeholder="Name"
                />
                <input
                    type="text"
                    name="bio"
                    value={newArtist.bio}
                    onChange={handleChange}
                    placeholder="Bio"
                />
                <button type="submit">Add Artist</button>
            </form>
            <ul>
                {artists.map((artist) => (
                    <li key={artist.id}>
                        {artist.name} - {artist.bio}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Artists;
