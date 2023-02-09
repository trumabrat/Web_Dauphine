import {
  Button,
  ButtonGroup,
  createTheme,
  CssBaseline,
  ThemeProvider,
  Typography,
} from "@mui/material";
import { Box, Container } from "@mui/system";
import { useState } from "react";
import "./App.css";
import CatFacts from "./components/CatFacts/CatFacts";
import GenderPredictor from "./components/GenderPredictor/GenderPredictor";

const theme = createTheme();

function App() {
  let [selection, setSelection] = useState("Cat Facts");
  const changeMode = (mode) => () => {
    setSelection(mode);
  }


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

              <Box sx={{ display: "flex", justifyContent: "center" }}>
                <ButtonGroup
                  variant="outlined"
                  aria-label="outlined button group"
                >
                  <Button onClick={changeMode("Cat Facts")}>Cat Facts</Button>
                  <Button onClick={changeMode("Gender Predictor")}>Gender Predictor</Button>
                </ButtonGroup>
              </Box>
            </Container>
          </Box>
          {selection === "Cat Facts" ? <CatFacts /> : <GenderPredictor />}
          
        </main>
      </ThemeProvider>
    </div>
  );
}

export default App;
