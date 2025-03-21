const express = require('express');
const app = express();
const port = 5000;
const fetch = (...args) => import('node-fetch').then(({ default: fetch }) => fetch(...args));

const axios = require('axios');
const chatRouter = require('./routes/chat');

// Set EJS as templating engine
app.set('view engine', 'ejs');
app.set('views', './views');

app.use(express.static('public')); 

// Middleware to add path to all views
app.use((req, res, next) => {
    res.locals.path = req.path;
    next();
});

// Routes
app.get('/', (req, res) => {
    res.render('homepage', { title: 'Home - ArthSathi' });
});

app.get('/about', (req, res) => {
    res.render('about', { title: 'About Us - ArthSathi' });
});

app.get('/news', async (req, res) => {
    try {
        // Fetch Latest Financial News
        const newsResponse = await fetch('https://newsapi.org/v2/top-headlines?category=business&country=in&apiKey=YOUR_NEWSAPI_KEY');
        const newsData = await newsResponse.json();
        const news = newsData.articles.map(article => ({

            title: article.title,
            description: article.description,
            url: article.url,
            image: article.urlToImage || 'default-news-image.jpg',
            date: new Date(article.publishedAt).toLocaleDateString()
        }));

        // Fetch NIFTY 50 Stock Market Data
        const stocksResponse = await fetch('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=NIFTY50&interval=5min&apikey=YOUR_ALPHAVANTAGE_KEY');
        const stocksData = await stocksResponse.json();
        const latestTime = Object.keys(stocksData['Time Series (5min)'])[0];
        const latestStock = stocksData['Time Series (5min)'][latestTime];

        const stocks = [{
            company: 'NIFTY 50',
            symbol: 'NIFTY50',
            price: parseFloat(latestStock['1. open']).toFixed(2),
            change: (parseFloat(latestStock['4. close']) - parseFloat(latestStock['1. open'])).toFixed(2),
            percent_change: ((parseFloat(latestStock['4. close']) - parseFloat(latestStock['1. open'])) / parseFloat(latestStock['1. open']) * 100).toFixed(2)
        }];

        // Fetch Economic Indicators (GDP, Inflation, Budget Deficit)
        const economicResponse = await fetch('https://api.economicdata.com/india');
        const economicData = await economicResponse.json();

        res.render('news', {
            title: "Latest Financial News",
            news,
            stocks,
            economicData: {
                gdp: economicData.gdp_growth,
                inflation: economicData.inflation_rate,
                budgetDeficit: economicData.budget_deficit
            }
        });

    } catch (error) {
        console.error('Error fetching data:', error);
        res.render('news', { news: [], stocks: [], economicData: {} });
    }
});


app.get('/contributors', (req, res) => {
    res.render('contributors', { title: 'Contributors - ArthSathi' });
});

app.get('/contact', (req, res) => {
    res.render('contact', { title: 'Contact - ArthSathi' });
});

app.get('/help', (req, res) => {
    res.render('help', { title: 'Help - ArthSathi' });
});

app.get('/login', (req, res) => {
    res.render('login', { title: 'Login - ArthSathi' });
});

app.get('/register', (req, res) => {
    res.render('register', { title: 'Register - ArthSathi' });
});

app.get('/explore', (req, res) => {
    res.render('explore', { title: 'Explore - ArthSathi' });
});

// Add chat route
app.use(chatRouter);

// Add dashboard routes
app.get('/dashboard', (req, res) => {
    res.render('data', { 
        title: 'Market Data - ArthSathi'
    });
});

app.get('/dashboard/financial-data', (req, res) => {
    res.render('financial_data', { 
        title: 'Financial Data - ArthSathi'
    });
});

// Error handler for 404
app.use((req, res) => {
    res.status(404).render('404', { title: '404 - Page Not Found' });
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
