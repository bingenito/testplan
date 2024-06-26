from testplan.runners.pools.tasks.base import task_target
from testplan.testing.multitest import MultiTest, testcase, testsuite


@task_target
def dummy_test():
    return MultiTest(name="dummy_test", suites=[Suite()])


@testsuite
class Suite:
    @testcase
    def case_1(self, env, result):
        result.true(True)

    @testcase
    def case_2(self, env, result):
        result.false(False)

    @testcase
    def case_3(self, env, result):
        result.true(True)
