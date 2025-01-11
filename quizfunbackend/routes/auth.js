const User = require('./User');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const express = require('express');
const router = express.Router();

router.post('/signup', async (req, res) => {
    try {
        const {username, email, password} = req.body;
        const oldUser = await User.findOne({ $or: [{email}, {username}]});
        if (oldUser) {
            return res.status(400).json({error: 'User with this email or username already exists'});
        }
        const user = new User({username, email, password})
        await user.save();
        res.status(201).json({message: 'Account created successfully'})
    }catch (err){
        res.status(400).json({error: err.message})
    }
});


router.post('/login', async (req, res) => {
    try {
        const {username, email, password} = req.body;
        const user = await User.findOne({$or:[{email}, {username}]});
        if (!user) {
            return res.status(400).json({ error: 'Account not found, try signing up' });
        }
        const passwordMatch = await bcrypt.compare(password, user.password);
        if (!passwordMatch) {
            return res.status(400).json({ error: 'Incorrect password' });
        }

        const token = jwt.sign({userId: user._id}, 'secret_key');
        res.json({token});
    }catch (err) {
        res.status(400).json({error: err.message})
    }
})

module.exports = router;