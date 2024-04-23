import React, { useState, useEffect } from 'react';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import background from '../images/background.jpg';

function Home() {
  const [motto, setMotto] = useState("Be Stronger");
  const mottos = ["Be Stronger", "Be Fitter", "Become a GymRat"];

  useEffect(() => {
    const intervalId = setInterval(() => {
      setMotto((prevMotto) => {
        const nextIndex = (mottos.indexOf(prevMotto) + 1) % mottos.length;
        return mottos[nextIndex];
      });
    }, 3000); // Zmienia motto co 3 sekundy

    return () => clearInterval(intervalId); // Czyszczenie interwału
  }, []);

  return (
    <Container maxWidth="x1"
    sx={{ 
      backgroundImage: `url(${background})`,
      minHeight: '90vh',
      backgroundSize: 'cover',
     }}>
      <Box 
      sx={{ 
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',

       }}>
        <Typography variant="h4" component="h1" gutterBottom color="secondary">
          Welcome to the GymRattttt
        </Typography>
  
        <Typography variant="h5" gutterBottom color="secondary">
          {motto === "Be a GymRat" ? (
            <span>
              {"Be a "}
              
            </span>
          ) : (
            motto
          )}
        </Typography>
      </Box>
    </Container>
  );
}

export default Home;