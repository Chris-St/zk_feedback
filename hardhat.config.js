/** @type import('hardhat/config').HardhatUserConfig */
require("@nomiclabs/hardhat-waffle");
require("dotenv").config(); // Load environment variables

module.exports = {
  solidity: "0.8.0",
  networks: {
    sepolia: {
      url: process.env.SEPOLIA_RPC_URL, // Use an environment variable for the RPC URL
      accounts: [`0x${process.env.PRIVATE_KEY}`], // Use an environment variable for the deployer's private key
    }
  }
};