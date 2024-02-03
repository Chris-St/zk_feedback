async function main() {
    // We get the contract to deploy
    const Contract = await ethers.getContractFactory("Feedback");
    const contract = await Contract.deploy(); // Add constructor arguments if needed
  
    console.log("Contract deployed to:", contract.address);
  }
  
  main()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error(error);
      process.exit(1);
    });
  