*** Settings ***
Library    SeleniumLibrary
Resource  ../Testcases/CreatePost.robot
Resource  ../Testcases/DeletePost.robot
Library    functions.py

*** Variables ***
${BROWSER}    Chrome
${URL}        https://react-redux.realworld.io/
${title_text}       krasny_den

*** Test Cases ***
Main
	[Documentation]  Hlavni modul na spusteni tasku
    Create and Publish New Post     ${title_text}
    Delete Post     ${title_text}
    #Test Post Creation      ${title_text}
