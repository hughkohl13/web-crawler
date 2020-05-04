const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const scrapeSchema = new Schema({
  company: { type: String, required: true },
  role: { type: String, required: true },
  url: String,
  date: { type: Date, default: Date.now }
});

const Scrape = mongoose.model("Scrape", scrapeSchema);

module.exports = Scrape;
