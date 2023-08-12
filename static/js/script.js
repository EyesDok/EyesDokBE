// DOM 요소를 선택
const eyeIcon = document.querySelector('.eye-icon');
const passwordInput = document.querySelector('.password');

eyeIcon.addEventListener('click', function() {
    // 비밀번호 입력 필드의 type이 'password'인지 확인
    if (passwordInput.type === 'password') {
        // 비밀번호를 보이게 변경
        passwordInput.type = 'text';
        // (선택적) 눈 아이콘 이미지나 스타일을 '비밀번호 보이기' 상태로 변경
        // 예: eyeIcon.style.backgroundImage = "url('path/to/open-eye.png')";
    } else {
        // 비밀번호를 숨기게 변경
        passwordInput.type = 'password';
        // (선택적) 눈 아이콘 이미지나 스타일을 '비밀번호 숨기기' 상태로 변경
        // 예: eyeIcon.style.backgroundImage = "url('path/to/closed-eye.png')";
    }
});
