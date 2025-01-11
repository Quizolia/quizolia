const mongoose = require("mongoose");

const quizfundb = async() => {
    try {
    await mongoose.connect('mongodb://localhost:27017/quiz-app');
    console.log('Database successfully connected');
    } catch (err) {
        console.log('Database connection error', err.message)
        console.log(err.stack)
    }
}

module.exports = quizfundb;