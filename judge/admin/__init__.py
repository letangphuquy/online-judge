from django.contrib import admin
from django.contrib.admin.models import LogEntry

from judge.admin.comments import CommentAdmin
from judge.admin.contest import ContestAdmin, ContestParticipationAdmin, ContestTagAdmin
from judge.admin.interface import (
    BlogPostAdmin,
    LicenseAdmin,
    LogEntryAdmin,
    NavigationBarAdmin,
)
from judge.admin.organization import OrganizationAdmin, OrganizationRequestAdmin
from judge.admin.problem import ProblemAdmin, ProblemPointsVoteAdmin
from judge.admin.profile import ProfileAdmin
from judge.admin.runtime import JudgeAdmin, LanguageAdmin
from judge.admin.submission import SubmissionAdmin
from judge.admin.taxon import ProblemGroupAdmin, ProblemTypeAdmin
from judge.admin.ticket import TicketAdmin
from judge.admin.volunteer import VolunteerProblemVoteAdmin
from judge.models import (
    BlogPost,
    Comment,
    CommentLock,
    Contest,
    ContestParticipation,
    ContestTag,
    Judge,
    Language,
    License,
    MiscConfig,
    NavigationBar,
    Organization,
    OrganizationRequest,
    Problem,
    ProblemGroup,
    ProblemPointsVote,
    ProblemType,
    Profile,
    Submission,
    Ticket,
    VolunteerProblemVote,
    Course,
)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentLock)
admin.site.register(Contest, ContestAdmin)
admin.site.register(ContestParticipation, ContestParticipationAdmin)
admin.site.register(ContestTag, ContestTagAdmin)
admin.site.register(Judge, JudgeAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
admin.site.register(MiscConfig)
admin.site.register(NavigationBar, NavigationBarAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(OrganizationRequest, OrganizationRequestAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(ProblemGroup, ProblemGroupAdmin)
admin.site.register(ProblemPointsVote, ProblemPointsVoteAdmin)
admin.site.register(ProblemType, ProblemTypeAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(VolunteerProblemVote, VolunteerProblemVoteAdmin)
admin.site.register(Course)
