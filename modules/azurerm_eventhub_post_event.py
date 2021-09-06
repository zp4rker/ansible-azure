from ansible.module_utils.azure_rm_common import AzureRMModuleBase

class AzureRMEventHubPostEvent(AzureRMModuleBase):

	def __init__(self):

		self.module_arg_spec = dict(
			connection_string=dict(type='str', required=True),
			event_format=dict(type='str', default='json'),
			event_data=dict(type='dict', required=True)
        )

        self.results = dict(
            changed=False
        )

        required_if = []

        self.connection_string = None
        self.event_format = None
        self.event_data = None

        super(AzureRMAutoScale, self).__init__(self.module_arg_spec, supports_check_mode=True, required_if=required_if)


    def exec_module(self, **kwargs):

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            setattr(self, key, kwargs[key])

        results = None
        changed = False

        self.results['msg'] = 'This is a message.'

        return self.results


def main():
	AzureRMEventHubPostEvent()


if __name__ == '__main__':
	main()    	