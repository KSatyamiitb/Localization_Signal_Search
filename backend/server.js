const cors = require('cors');
const express = require('express');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');
const app = express();
const PORT = 8000;

app.use(bodyParser.json());
app.use(cors());

app.get('/search', (req, res) => {
    const { query1, query2 } = req.query;
<<<<<<< HEAD
    console.log('Search query:', query1, query2);
=======
    console.log('Got Search query:', query1, query2);
>>>>>>> 502c76ef9897ea66def6b1279a754e041d283d28
    const pythonProcess = spawn('python3', ['./searchTarget.py', query1, query2]);
    pythonProcess.stdout.on('data', (data) => {
        console.log(`${data}`);
        res.send(data);
    });
});


app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

