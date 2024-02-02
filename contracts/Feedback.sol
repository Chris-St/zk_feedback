// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Feedback {
    struct FeedbackEntry {
        string message;
        uint256 timestamp;
    }

    FeedbackEntry[] private feedbacks;

    event FeedbackSubmitted(string message, uint256 timestamp);

    function submitFeedback(string calldata message) external {
        feedbacks.push(FeedbackEntry(message, block.timestamp));
        emit FeedbackSubmitted(message, block.timestamp);
    }

    function getFeedbackCount() external view returns (uint256) {
        return feedbacks.length;
    }

    function getFeedback(uint256 index) external view returns (string memory, uint256) {
        require(index < feedbacks.length, "Invalid index");
        FeedbackEntry storage entry = feedbacks[index];
        return (entry.message, entry.timestamp);
    }
}
