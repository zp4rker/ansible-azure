from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from azure.eventhub import EventHubProducerClient, EventData


def run_module():
    module_args = dict(
        connection_string=dict(type='str', required=True),
        event_format=dict(type='str', default='json'),
        event_data=dict(type='dict', required=True)
    )

    result = dict(
        changed=False,
        msg=None
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    client = EventHubProducerClient.from_connection_string(module.params['connection_string'])
    batch = client.create_batch()
    batch.add(EventData('Test message from Ansible'))

    with client:
        client.send_batch(batch)

    result['msg'] = 'This is a message.'

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
