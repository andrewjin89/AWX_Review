# 목차 #
- [AWX 메뉴 구성](#1)
  - [AWX 화면 구성(View)](#1-1)
- [Credentials 등록](#2)
  - [GitLab 연동](#2-1)
  - [Machine](#2-2)
- [Project 등록](#3)
- [Inventory 등록](#4)
  - [Host 등록](#4-1)
  - [Smart Inventory 등록](#4-2)
  - [Inventory Script 등록](#4-3)
- [Job Template 등록](#5)
  - [Job Template 등록](#5-1)
  - [Workflow Template 등록](#5-2)
- [Organizations 등록](#6)
- [User 등록](#7)
- [Teams 등록](#8)
- [Notifications 등록](#9)
- [Instance Groups 등록](#10)
---

<a name="1"></a>

## AWX 메뉴 구성 ##
|메뉴|내용|
|:-:|:-:|
|DASHBOARD|Job의 최근 실행 상태를 한눈에 볼 수 있는 화면|
|JOBS|최근 실행한 JOB 리스트|
|SCHEDULES|스케줄로 등록된 Job 리스트|
|PORTAL MODE|등록된 Job과 실행중인 Job을 하나의 화면에서 확인 가능|
|PROJECTS|playbook 모음을 하나의 단위로 묶어서 관리|
|CREDENTIALS|ansible 실행을 위한 계정 관리 메뉴 |
|CREDENTIAL TYPES|사용자 설정 인증 타입|
|INVENTORIES|Job을 실행하는 Host 모음|
|TEMPLATES|Inventory와 Playbook을 조합하여 실제 job이 실행되는 구성 단뒤 |
|ORGANIZATIONS|Users, Teams, Projects, Inventoryes의 최상위 묶음 단위|
|USERS|AWX 사용자 관리 메뉴|
|TEAMS|AWX 사용자 그룹 단위 |
|INVENTORY SCRIPTS|사용자 Inventory Script 관리 메뉴|
|NOTIFICATIONS|ansible의 실행 상태를 알려주는 알람 등록 화면|
|MANAGEMENT JOBS|Job 리스트나 실행 상태를 관리|
|INSTANCE GROUPS|Job을 실행하는 단위 그룹|
|SETTINGS|AWX의 인증과 기본 Job, ansible 설정을 관리|
> 자세한 내용은 [Ansible Tower 가이드 문서](http://docs.ansible.com/ansible-tower/)를 참고하면 된다.
---

<a name="1-1"></a>


## AWX 화면 구성(View) ##
- DASHBOARD 화면 예시![](images/2020-01-31-16-57-42.png)
  - 등록된 호스트 갯수
  - 등록된 인벤토리 갯수
  - 등록된 프로젝트 갯수
  - 연결 실패한 호스트 갯수
  - 동기화 실패한 인벤토리 갯수
  - 동기화 실패한 프로젝트 갯수
  - 등록된 Job 실행 성공(초록색) 및 실패(빨간색) 그래프
  - 최근 사용된 템플릿 현황
  - 최근 수행된 Job 리스트
- JOBS 화면 예시![](images/2020-01-31-16-59-33.png)
  - 전체 수행된 Job 리스트
    - 각 Job 클릭시 상세정보 표시
      - Job의 상세 정보
      - 성공 실패 등 상태 정보
      - 수행로그 정보
- SCHEDULES 화면 예시![](images/2020-01-31-16-59-45.png)
  - 등록된 Job리스트
  - 스케줄 설정 정보 
  - 다음 실행 시간 표시
---

<a name="2"></a>

## Credentials 등록 ##
![](images/2020-02-03-09-44-31.png)
- DETAILS
  - NAME**(필수)** : 등록할 인증정보에 대한 이름
  - CREDENTIAL TYPE**(필수)** : 등록할 인증 정보 종류
  - DESCRIPTION : 인정정보에 대한 설명
  - ORGANIZATION : 인증정보를 사용할 조직
- PERMISSIONS => 새로 만들 경우 저장 후 활성화 됨.
  - 인증정보를 사용할 계정이나 그룹을 지정한다.
---
<a name="2-1"></a>

### Git 연동 예시 ###
![](images/2020-02-03-09-50-23.png)
---
<a name="2-2"></a>

### Machine ###
![](images/2020-02-03-09-54-28.png)
---
<a name="3"></a>

## Project 등록 ##
---
<a name="4"></a>

## Inventory 등록 ##
---
<a name="4-1"></a>

### Host 등록 ###
---
<a name="4-2"></a>

### Smart Inventory 등록 ###
---
<a name="4-3"></a>

### Inventory Script 등록 ###
---
<a name="5"></a>

## Job Template 등록 ##
---
<a name="5-1"></a>

### Job Template 등록 ###
---
<a name="5-2"></a>

### Workflow Template 등록 ###
---
<a name="6"></a>

## Organizations 등록 ##
---
<a name="6"></a>

## User 등록 ##
---
<a name="8"></a>

## Teams 등록 ##
---
<a name="9"></a>

## Notifications 등록 ##
---
<a name="10"></a>

## Instance Groups 등록 ##