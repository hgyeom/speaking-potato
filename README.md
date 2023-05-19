스파르타 코딩클럽 내일배움캠프 본캠프 1주차 미니프로젝트 - 팀 소개 화면. React 1팀 : Speaking Potato

# Speaking Potato [24/7 올타임 레전드]

스파르타코딩클럽 6기_React / 23.05.15 ~ 23.05.19 

## 팀원

| 팀원   |  팀원구분 | 깃허브                                      | 블로그                                  |
| ------ | -------- | ------------------------------------------- | --------------------------------- |
| 김재영 | `팀장`   | https://github.com/jaeyoung9083  | https://dobby-factory.tistory.com/          |
| 김무겸 |  팀원     | https://github.com/hgyeom | https://frian.tistory.com/                        |    
| 이안진 |  팀원     | https://github.com/AJ3504 | https://lethargin.tistory.com/manage/posts        |
| 정송주 |  팀원     | https://github.com/songjuu | https://velog.io                                 |
| 최다연 |  팀원     | https://github.com/cheddaryeon     | https://velog.io/@cheddaryeon99          |

## 목차

-   [1. 프로젝트 소개](#1-프로젝트-소개)
-   [2. 프로젝트 시연 영상](#2-프로젝트-시연-영상)
-   [3. 프로젝트 주소](#3-프로젝트-주소)
-   [4. 프로젝트 S.A](#4-프로젝트-sa)
-   [5. 기술스택](#5-기술스택)
-   [6. 사용한 라이브러리](#6-사용한-라이브러리)
-   [7. API Table](#7-api-table)
-   [8. 구현기능](#8-구현-기능)

## 1. 프로젝트 소개

팀 Speaking potato의 팀원 소개 프로젝트명은 24/7 올타임 레전드입니다. 

저희는 1페이지, 2페이지, 3페이지로 구성하였고,

1페이지는 메인페이지로, 2페이지는 팀원 소개 페이지로, 3페이지는 방명록으로 구성되어 있습니다.

팀원 소개 페이지에서는 저희 팀원들의 성격 및 각오를 보실 수 있고, 방명록 페이지에서는 직접 코멘트를 남길 수 있습니다.

## 2. 프로젝트 시연 영상
[유튜브 링크](https://youtu.be/T-_IzOmaRBU)

## 3. 프로젝트 주소

https://github.com/hgyeom/speaking-potato

## 4. 프로젝트 S.A
https://teamsparta.notion.site/A-1-S-A-111709dce5ed43b5a5f3c53eb3e04db1

## 5. 기술스택
  * Javascript
  * html/css
  * Python
  * MongoDB

## 6. 사용한 라이브러리
  * JQuery
  * Bootstrap
  * Flask
  * Bs4
  * Pymongo
  * MongoDB

## 7. API Table

| Number | Method | URL                                   | Description     | Request                                                      | Response                                                     |
| ------ | ------ | ------------------------------------- | --------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1      | `POST` | /api/guestbook                          | 방명록 작성          | { ’name’: 닉네임, ‘comment’:코멘트, ’g_password’:비밀번호 } | POST /api/guestbook HTTP/1.1" 200 - { ’msg’:’방명록 저장완료’ } | 
| 2      | `PUT` | /api/guestbook                            | 방명록 수정           | { ’name’: 닉네임, ‘comment’:코멘트, ’_id’:고유번호, ’g_password’:비밀번호 }  |  PUT/api/guestbookHTTP/1.1" 200{ ‘msg’: ‘ 수정완료. } |                                
| 3      | `GET`  | /api/guestbook                            | 방명록 조회    |                   | GET /api/guestbook HTTP/1.1 200 { ’name’: 닉네임, ‘comment’:코멘트, ’_id’:고유번호, ’g_password’:게시글 비밀번호 }                                                             
| 4      | `GET`  | /api/guestbook                            | 방명록 삭제          |  { ’_id’:고유번호, ’g_password’:비밀번호 } | DELETE /api/guestbook HTTP/1.1" 200 - { ‘msg’:’삭제완료’ }                        
| 5      | `GET`  | /api/like                       | 응원하기   |  { like’:like } | PUT /api/like HTTP/1.1" 200 { ‘msg’:’💖응원 감자합니다!💖’ }
| 6      | `GET`  | /api//like                  | 응원수 조회  |       | GET /api/like HTTP/1.1" 200 - { ‘like_name’: 이름, ‘like’: 응원 수 } |


## 8. 구현 기능

### 1) 메인 페이지
<img width="1440" alt="스크린샷 2023-05-19 오전 9 56 03" src="https://github.com/hgyeom/speaking-potato/assets/131579657/b763c6b0-d418-45d5-99e8-3abf25d4f3d5">

### 2) 멤버 소개 페이지
<img width="1440" alt="스크린샷 2023-05-19 오전 9 56 32" src="https://github.com/hgyeom/speaking-potato/assets/131579657/33bf5f3c-c865-4832-874e-95c74e79b5bd">

### 3) 방명록
![image](https://github.com/hgyeom/speaking-potato/assets/131579657/3f5b87d8-1be1-4154-b1de-d97b2f2316f1)
