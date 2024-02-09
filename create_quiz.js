let questionCount = 0;

function addQuestion() {
    questionCount++;

    const questionDiv = document.createElement('div');

    questionDiv.innerHTML = `
        <h2>Question ${questionCount}</h2>
        <label for="question-${questionCount}">Question:</label>
        <input type="text" id="question-${questionCount}" name="question-${questionCount}"><br>

        <div id="answers-${questionCount}">
            <!-- Answers will be added here -->
        </div>

        <button type="button" onclick="addAnswer(${questionCount})">Add Answer</button>
    `;

    document.getElementById('quiz-questions').appendChild(questionDiv);
}

function addAnswer(questionNumber) {
    const answerDiv = document.createElement('div');

    answerDiv.innerHTML = `
        <label for="answer-${questionNumber}">Answer:</label>
        <input type="text" id="answer-${questionNumber}" name="answer-${questionNumber}">
        <input type="radio" id="correct-${questionNumber}" name="correct-${questionNumber}" value="answer-${questionNumber}">
        <label for="correct-${questionNumber}">Correct</label><br>
    `;

    document.getElementById(`answers-${questionNumber}`).appendChild(answerDiv);
}

window.onload = addQuestion;