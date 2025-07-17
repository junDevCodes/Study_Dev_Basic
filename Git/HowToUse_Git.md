# How to use Git

## git init
- 로컬 저장소를 초기화

## git add
- 변경된 파일을 Staging Area로 추가
- `git add .` : 전체 파일 추가  
- `git add 파일명` : 특정 파일만 추가

## git commit
- Staging Area의 파일을 Repository에 저장
- `git commit -m "메시지"` : 커밋 메시지와 함께 기록

## git commit --amend
- 직전 커밋 수정 (메시지 또는 파일)
- `git add 파일명` → `git commit --amend`
- VIM에서 `i`로 수정 → `:wq` 저장 후 종료
- `--no-edit` 옵션으로 메시지 그대로 유지 가능

## git restore --staged
- Staging Area에서 파일을 다시 Working Directory로 되돌림

## git status
- 현재 상태(변경됨, staged 여부 등)를 표시

## git log
- 커밋 로그 확인  
- 유용한 옵션:
    - `git log --oneline`
    - `git log --graph --all --decorate`

## 사용자 설정
- `git config --global user.email "이메일"`
- `git config --global user.name "이름"`
- `git config --global -l` : 현재 설정 보기

## git config --global alias.(단축어)
- 예: `git config --global alias.st status` → `git st`

## .gitignore
- 무시할 파일/폴더 정의
- 이미 추적 중인 파일은 `git rm --cached`로 캐시 제거 후 제외 처리

## git revert <commit_id>
- 기존 커밋 내용을 반대로 적용하여 **새 커밋 생성**
- 안전하게 변경 취소 가능

### revert 확장 명령어
- `git revert a1b2c3 d4e5f6` : 여러 커밋 revert
- `git revert a1b2..d4e5` : 범위 지정
- `git revert --no-edit` : 메시지 편집 생략
- `git revert --no-commit` : revert만 staging

## git reset [옵션] <commit_id>
- 특정 커밋 시점으로 되돌림  
- **주의**: 이후 커밋들이 삭제될 수 있음!

### 옵션별 의미
- `--soft` : Staging Area에만 유지
- `--mixed` : Working Directory로 되돌림 (기본값)
- `--hard` : 모든 이력 제거 (복구 불가 ⚠️)

## git reflog
- HEAD의 이동 이력 추적 (삭제된 커밋도 포함)
- `git reset --hard <복구할 커밋>` 으로 복원 가능

## Undoing / git restore
- Working Directory 변경 전 상태로 되돌리기
- `git restore 파일명` → 수정 내용 덮어씀 ⚠️

## Unstage
- `git restore --staged 파일명` : staged 해제
- `git rm --cached 파일명` : 저장소에서 추적 제거
