# Copyright OpenSearch Contributors
# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
from core.object_store.types import ObjectStoreType


def test_object_store_type_values():
    assert ObjectStoreType.S3 == "s3"
