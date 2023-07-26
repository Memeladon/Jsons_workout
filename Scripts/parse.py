import json
import os
import time


class Parse:
    def __init__(self, path):
        # folder_path - Путь к папке с JSON-файлами
        self.main_folder_path = path

        '''
        DB.Metrics.Status - состояние MySQL. SHOW GLOBAL STATUS         #! not using
        DB.Metrics.Latency - Latency в момент сбора
        DB.Conf - полная конфигурация MySQL                             
        System - информация о система CPU, Memory                       #! not using
        '''

        # self.db_metrics_status = []
        self.db_metrics_latency = []
        self.db_conf = []
        # self.system = []
        self.global_arr = []

        self.keys = ['binlog_cache_size', 'binlog_group_commit_sync_delay', 'binlog_group_commit_sync_no_delay_count',
                     'binlog_max_flush_queue_time', 'binlog_stmt_cache_size', 'eq_range_index_dive_limit',
                     'host_cache_size', 'innodb_adaptive_hash_index_parts', 'innodb_adaptive_max_sleep_delay',
                     'innodb_autoextend_increment', 'innodb_buffer_pool_chunk_size', 'innodb_buffer_pool_dump_pct',
                     'innodb_buffer_pool_instances', 'innodb_buffer_pool_size', 'innodb_change_buffer_max_size',
                     'innodb_change_buffering', 'innodb_commit_concurrency', 'innodb_compression_failure_threshold_pct',
                     'innodb_compression_level', 'innodb_compression_pad_pct_max', 'innodb_concurrency_tickets',
                     'innodb_dedicated_server', 'innodb_disable_sort_file_cache', 'innodb_doublewrite_batch_size',
                     'innodb_doublewrite_files', 'innodb_doublewrite_pages', 'innodb_flush_log_at_timeout',
                     'innodb_flush_neighbors', 'innodb_flush_sync', 'innodb_flushing_avg_loops', 'innodb_ft_cache_size',
                     'innodb_ft_result_cache_limit', 'innodb_ft_sort_pll_degree', 'innodb_ft_total_cache_size',
                     'innodb_io_capacity', 'innodb_io_capacity_max', 'innodb_lock_wait_timeout',
                     'innodb_log_buffer_size', 'innodb_log_file_size', 'innodb_log_files_in_group',
                     'innodb_log_spin_cpu_abs_lwm', 'innodb_log_spin_cpu_pct_hwm', 'innodb_log_wait_for_flush_spin_hwm',
                     'innodb_log_write_ahead_size', 'innodb_lru_scan_depth', 'innodb_max_dirty_pages_pct',
                     'innodb_max_dirty_pages_pct_lwm', 'innodb_max_purge_lag', 'innodb_max_purge_lag_delay',
                     'innodb_max_undo_log_size', 'innodb_old_blocks_pct', 'innodb_old_blocks_time',
                     'innodb_online_alter_log_max_size', 'innodb_page_cleaners', 'innodb_page_size',
                     'innodb_purge_batch_size', 'innodb_purge_rseg_truncate_frequency', 'innodb_purge_threads',
                     'innodb_random_read_ahead', 'innodb_read_ahead_threshold', 'innodb_read_io_threads',
                     'innodb_replication_delay', 'innodb_rollback_segments', 'innodb_sort_buffer_size',
                     'innodb_spin_wait_delay', 'innodb_sync_array_size', 'innodb_sync_spin_loops',
                     'innodb_thread_concurrency', 'innodb_thread_sleep_delay', 'innodb_use_native_aio',
                     'innodb_write_io_threads', 'join_buffer_size', 'lock_wait_timeout', 'max_binlog_cache_size',
                     'max_binlog_size', 'max_binlog_stmt_cache_size', 'max_delayed_threads', 'max_heap_table_size',
                     'max_insert_delayed_threads', 'max_join_size', 'max_length_for_sort_data', 'max_relay_log_size',
                     'max_seeks_for_key', 'max_sort_length', 'max_sp_recursion_depth', 'max_tmp_tables',
                     'max_write_lock_count', 'metadata_locks_cache_size', 'open_files_limit', 'optimizer_prune_level',
                     'optimizer_search_depth', 'parser_max_mem_size', 'preload_buffer_size', 'query_alloc_block_size',
                     'query_cache_limit', 'query_cache_min_res_unit', 'query_cache_size', 'query_cache_type',
                     'query_cache_wlock_invalidate', 'query_prealloc_size', 'range_alloc_block_size',
                     'range_optimizer_max_mem_size', 'read_buffer_size', 'read_rnd_buffer_size',
                     'relay_log_space_limit', 'rpl_read_size', 'rpl_stop_slave_timeout', 'slave_allow_batching',
                     'slave_checkpoint_group', 'slave_checkpoint_period', 'slave_parallel_type',
                     'slave_parallel_workers', 'slave_pending_jobs_size_max', 'sort_buffer_size',
                     'stored_program_cache', 'stored_program_definition_cache', 'table_definition_cache',
                     'table_open_cache', 'table_open_cache_instances', 'tablespace_definition_cache',
                     'temptable_max_ram', 'thread_cache_size', 'thread_stack', 'timed_mutexes', 'tmp_table_size',
                     'transaction_alloc_block_size', 'transaction_prealloc_size']

    @staticmethod
    def is_numeric(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def read_mining(self):
        # Получаем список папок
        folders_list = os.listdir(self.main_folder_path)
        folders_list.remove('.idea')

        # Проходимся по каждой папке
        for folder_name in folders_list:
            # Формируем полный путь к файлу
            files_list = os.listdir(self.main_folder_path + f'/{folder_name}')

            print(folder_name)

            # Проходим по каждому json'у
            for file_name in files_list:
                file_path = self.main_folder_path + f'/{folder_name}' + f'/{file_name}'
                # print(file_path)

                # Проверяем, является ли файл JSON-файлом
                if file_name.endswith('.json'):
                    # Открываем JSON-файл для чтения
                    with open(file_path, 'r') as file:
                        # Загружаем JSON-данные
                        json_data = json.load(file)

                        # Проверяем, присутствует ли ключ в JSON-данных
                        if 'DB' and 'System' in json_data:
                            if json_data['DB']['Metrics']['Latency'] is not None:

                                hashes = {'Latency': json_data['DB']['Metrics']['Latency']}
                                for key, value in json_data['DB']['Conf']['Variables'].items():
                                    for item in self.keys:
                                        if key == item:
                                            if value is not None and self.is_numeric(value):
                                                hashes[key] = float(value)

                                self.global_arr.append(hashes)

        return self.global_arr
