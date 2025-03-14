import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { setCredentials } from "../features/user/userSlice";
import { TextField, Button, Container, Typography } from "@mui/material"; 
import axios from "axios";
import qs from "qs";

const Login: React.FC = () => {
    const dispatch = useDispatch();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async () => {
        try {
            const data = qs.stringify({
                username: email,
                password: password,
            });
            const response = await axios.post("http://localhost:8000/user/token", data, {
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                }
            });
            dispatch(setCredentials({ token: response.data.access_token, username: email }));
            alert("Login successful!");
        } catch (error: any) {
            console.error("Login failed:", error);
            alert("Error logging in: " + (error.response ? error.response.data.detail : error.message));
        }
    };

    return (
        <Container maxWidth="sm">
            <Typography variant="h4" gutterBottom>
                Login
            </Typography>
            <TextField
                label="Email"
                fullWidth
                margin="normal"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />
            <TextField
                label="Password"
                type="password"
                fullWidth
                margin="normal"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            <Button 
                variant="contained" 
                color="primary" 
                fullWidth 
                onClick={handleLogin}
            >
                Log In
            </Button>
        </Container>
    );
};

export default Login;