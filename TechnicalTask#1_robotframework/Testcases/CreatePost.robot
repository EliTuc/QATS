*** Settings ***
Library         SeleniumLibrary
#Resource        ../Resources/Settings.robot
#Library        functions.py
*** Variables ***
${URL}        https://react-redux.realworld.io/
${username}=     tech_task@qats.sk
${pass}     124lkjAF89as
${vSignin}=  xpath://a[text()='Sign in']
${vEmail}=  xpath://input[@type='email']
${vPass}=   xpath://input[@type='password']
${vSubmit}=  xpath://button[@type='submit']
${vNewPost}=  xpath:(//li[@class='nav-item'])[2]
${vPublish}=  xpath://button[text()='Publish Article']
${vTitle}=  xpath://input[@placeholder='Article Title']
${vDescription}=  xpath://input[@class='form-control']
${vText}=  xpath://textarea[@class='form-control']
${article_exist}=  xpath://div[@class="article-meta"]
${vSettings}=  xpath://i[@class="ion-gear-a"]
${vLogout}=  xpath://button[@class="btn btn-outline-danger"]
*** Keywords ***
Login
	Create Webdriver    Chrome
    Go To   ${URL}
    Wait Until Element Is Visible    ${vSignin}      5
    Click Element    ${vSignin}
    Input Text    ${vEmail}    ${username}
    Input Text    ${vPass}    ${pass}
    Click Element    ${vSubmit}
    Log To Console    Sign in succesful

Logout
    Click Element    ${vSettings}
    Click Element    ${vLogout}
    Log To Console    Logout Succesful

Create and Publish New Post
	[Arguments]    ${title_text}
    #add new post
    Login
    Sleep  3
    Wait Until Element Is Visible    ${vNewPost}      7
    ${buttonText}=    Get Text    ${vNewPost}
    Log To Console    buttonText${buttonText}
    Click Element    ${vNewPost}
    Input Text    ${vTitle}    ${title_text}
    Input Text    ${vDescription}    Popisek
    Input Text    ${vText}    Text je povinný
    Click Element    ${vPublish}

    #check if stribut exists
    ${status}=    Run Keyword And Return Status    Element Should Exist    ${article_exist}
        Run Keyword If    ${status}    Log    Element exists
         ...    ELSE    Log    příspěvek nepřidán
    Logout

