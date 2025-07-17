# How to use Git

## git init
- 깃 초기화

## git add
- 변경사항이 있는 파일을 staging area로 추가
- ex) git add . (전체 파일 추가) / git add 파일명 (특정 파일 추가)

## git commit
- staging area에 있는 파일들을 repository에 기록
- ex) git commit -m "commit msg" (-m "커밋 메세지"를 통해 기록 남기기 가능)

## git commit --amend
- 직전 커밋 메시지 / 커밋 내용 수정
- git commit --amend 실행 시 VIM 실행
- VIM 내부에서 i 입력 시 INSERT MODE -> commit msg 수정
- 추가할 파일이 있다면 git add (파일명) 이후 git commit --amend
- VIM 탈출 = :wq (w : write, q : quit)

## git restore --staged
- git restore --staged (파일명) 을 통해 add 한 파일 취소 가능

## git status
- working area, staging area의 상태 표시

## git log
- repository에 기록된 log 불러오기

## git flow
[![image.png](https://i.postimg.cc/J7gFDGDS/image.png)](https://postimg.cc/Z08HXYLL)

## 사용자 설정
- git config --global user.email "메일 주소"
- git config --global user.name "유저 네임"
- git config --global -l : global 설정 정보 확인

## git config --global alias.(단축어) 명령
- 원하는 명령을 단축키 생성 가능
- ex) git config --global alias.st status
- git st == git status

## .gitignore
- gitignore 파일에 등록하여 git에 push되지 않도록 한다
- 한번 원격 저장소에 올라간 파일은 끝까지 추적되기 때문에 이 경우 git rm --cached를 통해 캐시를 제거하고 무시처리해야한다.