// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import the contract to test
import "../contracts/Feedback.sol";
// Hardhat's test helpers
import "hardhat/console.sol";

contract FeedbackTest {
    Feedback feedback;

    // This runs before each test, setting up the environment
    function beforeEach() public {
        feedback = new Feedback();
    }

    // Example test: Ensure feedback can be submitted and retrieved
    function testSubmitAndRetrieveFeedback() public {
        string memory testMessage = "Test feedback message";
        feedback.submitFeedback(testMessage);
        (string memory returnedMessage, ) = feedback.getFeedback(0);

        // Use Hardhat's console to output values during testing
        console.log("Submitted message:", testMessage);
        console.log("Retrieved message:", returnedMessage);

        // Assert that the submitted message matches the retrieved one
        assert(keccak256(abi.encodePacked(returnedMessage)) == keccak256(abi.encodePacked(testMessage)));
    }
}
