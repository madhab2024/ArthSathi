const express = require('express');
const router = express.Router();
const { spawn } = require('child_process');

// Route for news and sentiment analysis page
router.get('/', (req, res) => {
    // Sample data - in a real app, this would come from your database or API
    const sampleData = {
        title: 'News & Financial Updates - ArthSathi',
        news: [
            {
                title: 'Market Update: NIFTY Reaches New High',
                description: 'Indian markets show strong momentum as NIFTY crosses previous records.',
                image: '/images/market-update.jpg',
                url: '#',
                date: new Date().toLocaleDateString()
            },
            {
                title: 'RBI Announces Policy Changes',
                description: 'Reserve Bank of India introduces new measures to stabilize the economy.',
                image: '/images/rbi-update.jpg',
                url: '#',
                date: new Date().toLocaleDateString()
            }
        ],
        stocks: [
            {
                company: 'TCS',
                symbol: 'TCS.NS',
                price: '3450.75',
                change: '+45.30',
                percent_change: '+1.32'
            },
            {
                company: 'Infosys',
                symbol: 'INFY.NS',
                price: '1478.25',
                change: '-12.45',
                percent_change: '-0.84'
            }
        ],
        economicData: {
            gdp: '6.8',
            inflation: '4.2',
            budgetDeficit: '17.5'
        }
    };

    res.render('news', sampleData);
});

// API endpoint to get sentiment analysis
router.post('/analyze', (req, res) => {
    const { text } = req.body;
    
    // Spawn Python process
    const pythonProcess = spawn('python', ['scripts/sentiment_analysis.py', text]);
    
    let result = '';
    
    pythonProcess.stdout.on('data', (data) => {
        result += data.toString();
    });
    
    pythonProcess.stderr.on('data', (data) => {
        console.error(`Error: ${data}`);
    });
    
    pythonProcess.on('close', (code) => {
        if (code !== 0) {
            return res.status(500).json({ error: 'Failed to analyze sentiment' });
        }
        try {
            const sentiment = JSON.parse(result);
            res.json(sentiment);
        } catch (error) {
            res.status(500).json({ error: 'Invalid response from analyzer' });
        }
    });
});

module.exports = router; 