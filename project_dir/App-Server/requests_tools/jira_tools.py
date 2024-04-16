from jira import JIRA



def search_all_comments_in_issue(issue):
    '''Return dict with all issue key is name autor of comment, value is list with all comment this autor.   Function accepts an object of type issue.'''
    all_comment_in_issue = {
        'task_id': issue.id, 
        'task_name': issue.key,
        'task_publication_time': issue.fields.created,
        'messages': [

        ]
    }
    if len(issue.fields.comment.comments):
        for comment in issue.fields.comment.comments:
            all_comment_in_issue['messages'].append(
                {
                    'issue' : issue.key,
                    'url_issue' : 'https://jira.korona.net/browse/' + issue.key + '?focusedCommentId=' + comment.id,
                    'text': comment.body,
                    'message_id': comment.id,
                    'message_publication_time':comment.created,
                    'user_id':comment.author.name,
                    'edit' : comment.created != comment.updated,
                    'edit_date' : comment.updated,
                }
            )
            

    return all_comment_in_issue          


def serch_all_issue_in_project(jira,name_project):
    '''return all issue in project. Function accepts names of project type string.'''
    all_issue = jira.search_issues('project' + name_project)
    return all_issue


def serch_all_projects(jira):
    '''return list of name all projects on jira. function accpets object type jira.'''
    return jira.projects() 
    
def search_all_comment_in_project(jira,name_project):
    '''return dict key = author name of comment value = list of all coment. Function accept name project type string'''
    all_issue = jira.search_issues('project' + name_project) 
    all_comment = {}
    for issue in all_issue:
        if issue.name not in all_comment:
            all_comment[issue.name] = [issue.body]
        else:
            all_comment[issue.name].append(issue.body) 
    return all_issue          

