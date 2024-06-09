import React from 'react';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import Artifacts from './components/Artifacts';
import Artists from './components/Artists';
import Users from './components/Users';
import LoginPage from './components/LoginPage'; // Import the login page component

function App() {
    return (
        <Router>
            <div>
                <nav>
                    <ul>
                        <li>
                            <Link to="/artifacts">Artifacts</Link>
                        </li>
                        <li>
                            <Link to="/artists">Artists</Link>
                        </li>
                        <li>
                            <Link to="/users">Users</Link>
                        </li>
                        <li>
                            <Link to="/login">Login</Link>
                        </li>
                    </ul>
                </nav>
                <Routes>
                    {/* Set the default route to the login page */}
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/artifacts" element={<Artifacts />} />
                    <Route path="/artists" element={<Artists />} />
                    <Route path="/users" element={<Users />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
