import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function LoginPage() {
    const [formData, setFormData] = useState({ username: '', password: '' });
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        console.log(formData);
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:5000/login', formData, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            // Handle successful login, e.g., store user info and redirect
            console.log(response.data);
            
            navigate('/artists'); // Redirect to artifacts page on success
        } catch (error) {
            // Handle login error
            setError('Invalid username or password');
        }
    };

    return (
        <div>
            <h1>Login</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="username">Username</label>
                <input
                    type="text"
                    id="username"
                    name="username"
                    value={formData.username}
                    onChange={handleChange}
                />
                <label htmlFor="password">Password</label>
                <input
                    type="password"
                    id="password"
                    name="password"
                    value={formData.password}
                    onChange={handleChange}
                />
                <button type="submit">Login</button>
            </form>
            {error && <p>{error}</p>}
            <p>Don't have an account? <a href="/register">Register</a></p>
        </div>
    );
}

export default LoginPage;
