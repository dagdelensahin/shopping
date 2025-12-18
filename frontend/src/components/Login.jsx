import React from 'react'
import { useState } from "react";
import { useNavigate } from "react-router-dom";


function Login() {
    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const handleSubmit = async(e) => {
        e.preventDefault();
        setLoading(true);
        setError("");
        // Handle login logic here
        console.log("Logging in with", { username, password });

        if(!username || !password) {
            alert("Please enter both username and password");
            return;
        } 

        try {
            const response = await fetch("http://localhost:5000/api/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ username, password }),
            });
            const data = await response.json();
            localStorage.setItem("token", data.token);

            if (response.ok) {
                console.log("Login successful:", data);
                // Redirect or update UI accordingly
                navigate("/dashboard", { replace: true });
            } else {
                 alert(data.error || "Login failed");
            }
        } catch (err) {
            alert(err.message || "An error occurred. Please try again.");
            setError("An error occurred. Please try again.");
        } finally {
            setLoading(false);
        }
    };


    return (      
          <form onSubmit={handleSubmit}>
             <h2>Login</h2>
                {error && <p style={{ color: "red" }}>{error}</p>}
                <div>
                    <label>Username:</label>
                    <input
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>

                <div>
                    <label>Password:</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />  
                </div>

                <button type="submit" disabled={loading}>
                    {loading ? "Logging in..." : "Login"}
                </button>
</form>
    );
}

export default Login;


 

  
 