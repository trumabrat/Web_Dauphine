import {
  createTheme,
  CssBaseline,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  ThemeProvider,
  Typography,
} from "@mui/material";
import { Box, Container } from "@mui/system";
import { useState } from "react";
import "./App.css";
import CatFacts from "./components/CatFacts/CatFacts";

const theme = createTheme();

function App() {
  let [selection, setSelection] = useState("Cat Facts");
  const handleChange = (event) => {
    console.log(event.target.value);
  };

  return (
    <div className="App">
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <main>
          <Box
            sx={{
              bgcolor: "background.paper",
              pt: 8,
              pb: 6,
            }}
          >
            <Container maxWidth="sm">
              <Typography
                component="h1"
                variant="h2"
                align="center"
                color="text.primary"
                gutterBottom
              >
                Problem Set 3.1
              </Typography>
              <Typography
                variant="h5"
                align="center"
                color="text.secondary"
                paragraph
              >
                Please find below my solutions to the problems in Problem Set
                3.1 of the course. I hope that you don't mind the fact that I've
                integrated the solutions into a single React app.
              </Typography>

              <FormControl fullWidth direction="row" justifyContent="center">
                <InputLabel id="select-mode-label">Select mode</InputLabel>
                <Select
                  labelId="select-mode-label"
                  label="Select mode"
                  onClick={handleChange}
                >
                  <MenuItem value="Cat Facts">Cat Facts</MenuItem>
                  <MenuItem value="Gender predictor">Gender Predictor</MenuItem>
                </Select>
              </FormControl>
            </Container>
          </Box>
          <CatFacts />
        </main>
      </ThemeProvider>
    </div>
  );
}

export default App;
