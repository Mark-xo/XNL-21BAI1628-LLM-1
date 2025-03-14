import React, { useState } from "react";
import { Container, Typography, Button, TextField } from "@mui/material";
import axios from "axios";
import { useSelector } from "react-redux";
import { RootState } from "../app/store";

const Dashboard: React.FC = () => {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState("");
  const token = useSelector((state: RootState) => state.user.token);

  const handleQuery = async () => {
    try {
      const response = await axios.post(
        "http://localhost:8001/query/process_query",
        { query },
        { headers: { Authorization: "Bearer " + token } }
      );
      setResult(response.data.answer);
    } catch (error) {
      setResult("Error processing query");
    }
  };

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" gutterBottom>
        Financial Query Dashboard
      </Typography>
      <TextField
        label="Enter your financial query"
        fullWidth
        margin="normal"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <Button variant="contained" color="primary" onClick={handleQuery}>
        Ask Query
      </Button>
      {result && (
        <Typography variant="body1" sx={{ mt: 2 }}>
          {result}
        </Typography>
      )}
    </Container>
  );
};

export default Dashboard;
