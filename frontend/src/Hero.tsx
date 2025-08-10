import DocsGPT3 from './assets/cute_docsgpt3.svg';
import { useTranslation } from 'react-i18next';

export default function Hero({
  handleQuestion,
}: {
  handleQuestion: ({
    question,
    isRetry,
  }: {
    question: string;
    isRetry?: boolean;
  }) => void;
}) {
  const { t } = useTranslation();
  const demos = t('demo', { returnObjects: true }) as Array<{
    header: string;
    query: string;
  }>;

  return (
    <div className="text-black-1000 dark:text-bright-gray flex h-full w-full flex-col items-center justify-between">
      {/* Header Section */}
      <div className="flex grow flex-col items-center justify-center pt-8 md:pt-0">
        <div className="mb-4 flex flex-col items-center">
          <div className="mb-2 flex items-center">
            <span className="text-4xl font-semibold">K-AI</span>
            <img className="mb-1 inline w-14" src={DocsGPT3} alt="K-AI" />
          </div>
          <p className="text-lg text-gray-600 dark:text-gray-300 text-center max-w-md">
            Your intelligent pharmaceutical assistant for SOPs, GMP guidelines, and regulatory compliance
          </p>
        </div>
      </div>

      {/* Clean interface - no demo suggestions for pharmaceutical focus */}
    </div>
  );
}
