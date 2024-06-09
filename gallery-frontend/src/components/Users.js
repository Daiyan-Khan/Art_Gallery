import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Users() {
    const [users, setUsers] = useState([]);
    const [newUser, setNewUser] = useState({ username: '', email: '' });

    useEffect(() => {
        fetchUsers();
    }, []);

    const fetchUsers = async () => {
        const response = await axios.get('/users');
        setUsers(response.data);
    };
    const handleDeleteUser = async (userId) => {
        try {
            await axios.delete(`/users/${userId}`); // Delete request with artist ID
            const remainingUsers = users.filter(user => user.id !== userId);
            setUsers(remainingUsers);
        } catch (error) {
            console.error('Error deleting user:', error);
            // Handle error appropriately (e.g., display error message to the user)
        }
    };
      
    
    return (
        <div>
            <h1>Users</h1>
            <ol>
                {users.map((user) => (
                    <li key={user.id}>
                        {user.username} - {user.email}
                        <button onClick={() => handleDeleteUser(user.id)}>
              Delete
            </button>
                    </li>
                ))}
            </ol>
        </div>
    );
}

export default Users;
