import * as React from "react";
import Button from "@mui/material/Button";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { TextField } from "@mui/material";

export default function GenderPredictor() {
    let [name, setName] = React.useState("");
    let [gender, setGender] = React.useState("");
    const changeName = (event) => {
        setName(event.target.value);
    }
    const handleGuess = () => {
        fetch(`https://api.genderize.io?name=${name}`).then((response) => {
            response.json().then((data) => {
                setGender(data.gender)
            });
        });
    }
    return(
    <Container sx={{ py: 8 }}  maxWidth="md">
        <Typography style={{margin:10}}> Type the name, I guess the gender</Typography>
        <TextField style={{margin:10}} fullWidth id="outlined-basic" label="Outlined" variant="outlined" onChange={changeName} />
        <Button style={{margin:10}} variant="contained" onClick={handleGuess}>Guess</Button>
        {gender!=="" ? <Typography style={{margin:10, fontWeight: "bold"}}> The gender is {gender}</Typography> : null}
    </Container>
    )
}