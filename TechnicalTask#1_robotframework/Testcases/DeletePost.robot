*** Settings ***
Resource  ./CreatePost.robot
*** Variables ***
${vGlobal}=  xpath://a[text()='Global Feed']
${vHomepage}=  xpath://div[@class='home-page']
${vDeleteArticle}=  xpath://button[@class='btn btn-outline-danger btn-sm']
*** Keywords ***
Delete Post
	[Arguments]    ${title_text}
	Login
	Wait Until Element Is Visible    ${vGlobal}      2
	Click Element   ${vGlobal}
	Sleep    2
	Page Should Contain    ${title_text}
	Click Element    xpath://*[text()='${title_text}']
	Wait Until Element Is Visible    ${vDeleteArticle}      2
	Click Element    ${vDeleteArticle}
	Logout



