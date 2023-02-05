import * as React from "react";
import Button from "@mui/material/Button";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";

export default function CatFacts() {
  let [facts, setFacts] = React.useState([]);

  //api call
  const handleGetFact = () => {
    fetch("https://catfact.ninja/fact").then((response) => {
      response.json().then((data) => {
        setFacts([data.fact, ...facts]);
      });
    });
  };

  return (
    <Container sx={{ py: 8 }} maxWidth="md">
      {/* End hero unit */}
      <Grid container spacing={4}>
        <Grid item key="0" xs={12}>
          <Button variant="contained" onClick={handleGetFact}>
            Get fact
          </Button>
        </Grid>
        {facts.map((fact, index) => (
          <Grid item key={index} xs={12}>
            <Card
              sx={{
                height: "100%",
                display: "flex",
                flexDirection: "column",
                backgroundColor: "#b2ebf2",
              }}
            >
              <CardContent sx={{ flexGrow: 1 }}>
                <Typography>{fact}</Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
}
